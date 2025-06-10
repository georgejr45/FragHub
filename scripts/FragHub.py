import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QLabel, QProgressBar, QTabWidget
)
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt, pyqtSignal
from threading import Thread
import time
from GUI.tabs.tab_input import InputTab
from GUI.tabs.tab_output import OutputTab
from GUI.tabs.tab_filters import FiltersTab
from GUI.tabs.tab_output_settings import OutputSettingTab
from GUI.tabs.tab_projects import ProjectsTab
from progress_window import ProgressWindow
import platform

from MAIN import MAIN
import traceback
import ctypes

if platform.system() == "Windows":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("FragHub")


class MainWindow(QMainWindow):
    # Signal pour mettre à jour la barre de progression
    update_progress_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.MAIN_function = main_function_ref
        self.setWindowTitle("FragHub 1.3.1")
        self.setGeometry(100, 100, 1280, 720)

        # Création du layout principal
        main_layout = QVBoxLayout()

        # Ajouter le logo FragHub en haut
        banner = QLabel()
        pixmap = QPixmap("./GUI/assets/FragHub_icon.png").scaled(
            130, 130, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation
        )
        banner.setPixmap(pixmap)
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(banner)

        # Créez les onglets principaux
        self.tabs = QTabWidget()

        # Créer des instances explicites de OutputTab et ProjectsTab
        self.output_tab = OutputTab()
        self.projects_tab = ProjectsTab()

        # Ajouter les instances d'onglet à QTabWidget
        self.tabs.addTab(InputTab(), "INPUT")
        self.tabs.addTab(self.output_tab, "OUTPUT")
        self.tabs.addTab(FiltersTab(), "Filters settings")
        self.tabs.addTab(OutputSettingTab(), "Output settings")
        self.tabs.addTab(self.projects_tab, "Projects settings")
        main_layout.addWidget(self.tabs)

        # Connecter le signal (après avoir ajouté les onglets)
        self.output_tab.output_directory_changed.connect(self.projects_tab.output_directory_changed_signal)

        # Bouton START/STOP
        self.start_button = QPushButton("START")
        self.start_button.setFixedSize(140, 60)
        self.start_button.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.start_button.clicked.connect(self.open_progress_window)
        main_layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Ajouter le layout principal au widget central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Variables de contrôle
        self.running = False
        self.progress_window = None
        self.thread = None

    def open_progress_window(self):
        """
        Affiche la fenêtre de progression et masque la fenêtre principale (indépendante).
        """
        if not self.running:
            # Cacher la fenêtre principale pendant l'exécution
            self.hide()
            # Créer et montrer la fenêtre de progression
            # Assurez-vous que ProgressWindow est bien un QWidget ou QDialog
            self.progress_window = ProgressWindow(parent=None) # parent=None pour la rendre indépendante
            self.progress_window.show()
            # Démarrer l'exécution dans un thread séparé
            self.start_execution()

    def start_execution(self):
        """
        Lance l'exécution de MAIN() dans un thread séparé.
        """
        self.running = True
        self.thread = Thread(target=self.run_main_function, daemon=True)
        self.thread.start()

    def run_main_function(self):
        """
        Exécution de la tâche principale avec gestion de la progression.
        """
        try:
            # Lancement du processus principal
            MAIN(
                progress_callback=self.progress_window.update_progress_signal.emit,
                total_items_callback=self.progress_window.update_total_signal.emit,
                prefix_callback=self.progress_window.update_prefix_signal.emit,
                item_type_callback=self.progress_window.update_item_type_signal.emit,
                step_callback=self.progress_window.update_step_signal.emit,
                completion_callback=self.progress_window.completion_callback.emit,
                deletion_callback=self.progress_window.deletion_callback.emit,
            )
        except Exception as e:
            traceback.print_exc()
        finally:
            # Restaurer la fenêtre principale et terminer la progression
            self.show()  # Réaffiche la fenêtre principale
            if self.progress_window:
                self.progress_window.close()  # Ferme la fenêtre de progression
                self.progress_window = None
        except Exception as e:
        self.running = False  # S'assurer que l'état est correct

        if force_quit_app:
            QApplication.instance().quit()
        else:
            # Si on ne quitte pas l'app (ex: juste annuler la tâche),
            # s'assurer que la fenêtre principale est visible
            self.show()
            self.activateWindow()

    def closeEvent(self, event):
        """Gère la fermeture de la fenêtre principale par l'utilisateur (clic sur X)."""
        if self.running:
            reply = QMessageBox.question(self, 'Quitter FragHub ?',
                                         "Une tâche est en cours d'exécution.\n"
                                         "Voulez-vous vraiment arrêter la tâche et quitter ?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.clean_exit(force_quit_app=True)  # Tenter l'arrêt propre et quitter
                event.accept()  # Accepter la fermeture de la fenêtre

        else:
            # Pas besoin d'appeler clean_exit ici si on quitte juste l'appli
            # QApplication.quit() sera appelé par la fermeture normale
            event.accept()  # Accepter la fermeture

# --- Fin de MainWindow ---


# --- Worker pour les tâches de démarrage (NOUVEAU) ---
class StartupWorker(QObject):
    """Effectue les tâches de démarrage longues dans un thread séparé."""
    # Signal émis quand les tâches sont finies, passe la fonction MAIN importée
    finished = pyqtSignal(object)
    # Signal émis en cas d'erreur
    error = pyqtSignal(str)
    # Signal pour mettre à jour le message du splash screen
    update_splash_message = pyqtSignal(str, int)

    def __init__(self, base_dir):
        super().__init__()
        self._base_dir = base_dir

    def showMessage(self, message, font_size=28, alignment=Qt.AlignmentFlag.AlignCenter, color=Qt.GlobalColor.white):
        """Affiche un message dans le splash screen avec taille de police configurable."""
        self.message_label.setText(message)
        self.message_label.setAlignment(alignment)
        self.message_label.setStyleSheet(f"""
            QLabel {{
                color: white;
                font-weight: bold;
                font-size: {font_size}px;  /* Ajustement dynamique de la taille de la police */
            }}
        """)

    def run_startup_tasks(self):
        """Exécute l'importation et autres tâches longues."""
        try:
            # --- Tâche potentiellement longue 1 : Importation ---
            self.update_splash_message.emit("Loading FragHub, please wait...", 20)  # Message 1
            time.sleep(1)  # Simule un léger retard pour montrer le spinner

            # Importer le composant principal
            from scripts.MAIN import MAIN as imported_main

            # --- Tâche potentiellement longue 2 : Préparation ---
            self.update_splash_message.emit("Initializing main window", 20)  # Message 2
            time.sleep(1)

            # Émettre le signal de fin en cas de succès
            self.finished.emit(imported_main)

        except ImportError as e:
            error_msg = f"Failed to import 'scripts.MAIN': {e}\n{traceback.format_exc()}"
            print(f"ERROR in worker thread: {error_msg}")
            self.error.emit(error_msg)  # Émettre le signal d'erreur
        except Exception as e:
            error_msg = f"Unexpected error during startup tasks: {e}\n{traceback.format_exc()}"
            print(f"ERROR in worker thread: {error_msg}")
            self.error.emit(error_msg)  # Émettre le signal d'erreur


# --- Fin de StartupWorker ---
# --- Exception Hook Global ---
def exception_hook(exctype, value, tb):
    error_message = ''.join(traceback.format_exception(exctype, value, tb))
    sys.stderr.write(f"Uncaught exception:\n{error_message}")
    # Tenter d'afficher une QMessageBox même pour les erreurs non gérées
    try:
        # Vérifier si QApplication existe avant d'essayer de créer un widget
        if QApplication.instance():
             message_box = QMessageBox()
             message_box.setIcon(QMessageBox.Icon.Critical)
             message_box.setWindowTitle("Unhandled Exception")
             message_box.setText("An critical unexpected error occurred!")
             message_box.setDetailedText(error_message)
             # Définir une taille minimale pour la boîte de dialogue
             message_box.setMinimumSize(600, 300)
             # Tenter d'ajouter le texte détaillé dans une zone scrollable (si setDetailedText ne suffit pas)
             try:
                  text_edit = message_box.findChild(QTextEdit)
                  if text_edit:
                      text_edit.setMinimumSize(550, 200)
             except Exception:
                  pass # Ignorer si on ne peut pas trouver/modifier le QTextEdit
             message_box.exec()
        else:
             print("QApplication non disponible, impossible d'afficher QMessageBox pour l'erreur non gérée.")
    except Exception as e:
        print(f"Impossible d'afficher QMessageBox pour l'erreur non gérée: {e}")
    sys.exit(1)



# --- Fonction run_GUI (MODIFIÉE pour utiliser le threading) ---
def run_GUI():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./GUI/assets/FragHub_Python_icon.ico"))
    window = MainWindow()
    window.show()
    app.exec()


run_GUI()
