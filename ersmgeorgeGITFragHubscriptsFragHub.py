[33mcommit a1eedaf74a3b512262ec9daaab89e21a845fde45[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Merge: 200e275 9f9352f
Author: Methun George <methungeorge333@gmail.com>
Date:   Tue Jun 10 10:48:19 2025 +0200

    Merge remote-tracking branch 'upstream/main'
    
    X#      scripts/progress_window.py

[33mcommit 0972cd921afffdaa007fa227ae0049cf3e30992c[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Jun 5 14:59:52 2025 +0200

    Bump version to 1.3.2 and update documentation and labels accordingly. Adjust changelog with recent updates and refine deduplication logic in spectra handling.

[33mcommit 179ddc779a762e1fcfff58fdb79483e75c42113e[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Jun 5 14:42:00 2025 +0200

    Link ProgressWindow to parent MainWindow and refine stop button behavior.
    
    Refactored `ProgressWindow` initialization to accept a reference to its parent (`MainWindow`) for enhanced navigation. Updated stop button functionality to handle specific 'STOP' and 'FINISH' actions.

[33mcommit d1b683d7fae6db70b38dd34eb37ec615e1718ab8[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed May 14 13:57:44 2025 +0200

    Update version number to 1.3.1 across project files
    
    This commit updates the version number from 1.3.0 to 1.3.1 in the README, GUI titles, and related documentation. Ensures consistency and reflects the latest version release.

[33mcommit c8fe67fd208364e148892207bd3f549d649a6fcc[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Fri Apr 25 17:03:51 2025 +0200

    Set application icon dynamically based on platform.
    
    Updated the icon configuration to select the appropriate file based on the user's platform (Mac or others). Added a fallback mechanism if the icon is not found, with a warning message to notify the user. This ensures a consistent user experience across different environments.

[33mcommit 64694dc90977492f117af681873bc4c6eae9be57[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Fri Apr 25 16:59:54 2025 +0200

    Refactor error handling and task cancellation in GUI/MAIN
    
    Enhanced error handling with detailed QMessageBox and added support for task interruption via stop_flag. Improved cleanup logic, signal-slot connections, and traceability during GUI initialization and task execution.

[33mcommit f8a573c4270c7e77e0433cfc3fbcb43c08c86fa1[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Fri Apr 18 09:44:52 2025 +0200

    Use macOS-specific app icon format for compatibility.
    
    Updated the application icon handling to use `.icns` format on macOS, while retaining `.ico` for other platforms. This ensures proper icon display across different operating systems.

[33mcommit bd1e2fdbbf7b5e69effba486e0d0150be1f39e24[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Apr 17 09:40:55 2025 +0200

    Simplify AppUserModelID initialization logic
    
    Removed unnecessary try-except block around setting AppUserModelID. This eliminates redundant error handling and clarifies the code for Windows-specific functionality.

[33mcommit d54ae402b84b10bae696cd52f80138139a73e9cc[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Apr 16 16:58:29 2025 +0200

    Remove redundant exit code print statement
    
    The print statement displaying the application's exit code was unnecessary and has been removed to streamline the code. The application now directly exits with the appropriate code without additional output.

[33mcommit 42b525b1cfcf915399eb406d7e31f0c862055b4b[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Apr 16 15:30:41 2025 +0200

    `Fix AppUserModelID setting to target Windows platform only`
    
    The call to `SetCurrentProcessExplicitAppUserModelID` is now wrapped in a Windows-specific condition using `platform.system()`. This ensures compatibility by preventing the function from being invoked on non-Windows systems, avoiding potential errors.

[33mcommit 6a478cf3c63955df1ff9293eb7a309f4f2f4d405[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Apr 16 14:59:48 2025 +0200

    Add stream capturing and global exception handling
    
    Introduce the `StreamCapturer` class to capture and manage stdout/stderr streams, enabling logging and signal propagation. Implement a global exception hook to handle uncaught exceptions gracefully by displaying them in a QMessageBox and logging the errors. These changes improve error tracking and application robustness.

[33mcommit 6be58eb912a35f75685d5f247dbdc201093243d1[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Apr 16 14:54:48 2025 +0200

    Refactor splash screen message handling with font size support
    
    Updated the `showMessage` method to accept a configurable font size and adjusted styling via dynamic CSS. Modified signal and related function signatures to handle font size, improving flexibility and customization of splash screen messages.

[33mcommit 064a5d4ad00fe2b2e865d9b35357416a40b87192[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Apr 16 14:32:28 2025 +0200

    Add threading and UI enhancements to FragHub
    
    Implemented a threading model to separate startup tasks from the UI, reducing load time and improving responsiveness. Added a custom animated spinner widget and enhanced error handling and feedback in splash and main window workflows.

[33mcommit 8ba3da338012a1e022fd294410426ea458f07d61[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Apr 16 12:24:18 2025 +0200

    Add splash screen and error handling for application startup
    
    Introduced a splash screen for better user experience during application startup. Enhanced error handling for critical components, including deferred imports and application initialization, to provide informative feedback or graceful exits in case of failures. Also ensured smoother transition to the main window.

[33mcommit fb46e62fc0fddba09e9d9a4a33eb24fe9da01e6d[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Apr 14 19:06:28 2025 +0200

    Use `sys._MEIPASS` for base directory in PyInstaller builds.
    
    Replaced `os.path.dirname(sys.executable)` with `sys._MEIPASS` to correctly handle base directory resolution in PyInstaller environments. Updated file references to use `os.path.join(BASE_DIR, ...)` for dynamic path handling. This ensures compatibility for assets and scripts in both PyInstaller and regular Python script executions.

[33mcommit 017c65293419db95c36d8357fd923d005cc369d5[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Apr 14 18:49:46 2025 +0200

    Refactor paths to use BASE_DIR for dynamic asset resolution.
    
    Adjusted file paths to construct them dynamically using BASE_DIR, ensuring compatibility with both PyInstaller executables and script execution. This eliminates hardcoded paths and improves portability.

[33mcommit d070e9665bed6a18c187187097130cbe6ed421df[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Apr 14 17:12:06 2025 +0200

    Refactor imports for consistent script module referencing
    
    Updated all import statements to use explicit `scripts` prefixes for better module structure clarity and consistency. Adjusted dynamic paths and base directory definitions to ensure compatibility across execution methods (e.g., PyInstaller). Simplified and standardized various file path constructions.

[33mcommit ca60fbb77407a7525e4b80986da2234ec7219ba9[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Apr 14 14:11:04 2025 +0200

    Increase banner icon size to improve visual clarity.
    
    Updated the FragHub icon size from 130x130 to 200x200 in both `progress_window.py` and `FragHub.py`. This change enhances the banner's visibility and ensures better alignment with the overall UI design.

[33mcommit 0eef69ead0cdc4e1311436a7422a15ff1c5b8e3a[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Apr 14 10:49:37 2025 +0200

    Update version number to 1.3.0 in UI elements
    
    Updated the application window title from 1.2.6 to 1.3.0 in both `progress_window.py` and `FragHub.py`. This ensures the displayed version aligns with the latest release.

[33mcommit b4d5206fa23e5610e33adab7b40d01641af8bc5b[m
Merge: 70dc205 c7973a2
Author: Methun George <methungeorge333@gmail.com>
Date:   Fri Apr 4 13:10:38 2025 +0200

    Merge remote-tracking branch 'upstream/main'
    Bug fix

[33mcommit c7973a29453563be1fa10d37422bf0f31095304a[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Apr 3 15:11:51 2025 +0200

    Update version to 1.2.6 and fix MSP spectrum issue
    
    Bumped version references from 1.2.5 to 1.2.6 across the codebase and documentation. Addressed an issue where the last MSP spectrum was missing in some cases, improving file handling reliability.

[33mcommit b65a019dab3632c4045221752ca93263787cd59b[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Tue Mar 25 14:30:04 2025 +0100

    Update version number to 1.2.5 in window titles
    
    Updated the displayed version number from 1.2.4 to 1.2.5 in both `FragHub.py` and `progress_window.py` to reflect the latest version. This ensures consistency in the application's branding and versioning.

[33mcommit 6223069bec63e5992c80995a2a4465f20a4be84e[m
Author: René Meier <meier.rene@googlemail.com>
Date:   Tue Mar 25 12:42:50 2025 +0100

    Add check for windows to make project more cross-platform

[33mcommit 21e01a9930057d97b4069faa44a449f75aec3291[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Jan 27 11:52:26 2025 +0100

    Update version to 1.2.4 across application
    
    Bumped the application version from 1.2.3 to 1.2.4 in the README, main script, and progress window. This ensures the displayed version aligns with the updated release. No functional changes were made.

[33mcommit 7b607acd770a54c7683d63bbac2345d034a8abff[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Mon Jan 27 11:17:07 2025 +0100

    Enable dynamic toggle switch activation based on directory.
    
    The toggle switch in the ProjectsTab is now disabled by default and only becomes active when a valid `.fraghub` file is detected in the selected output directory. This update includes signal connections to manage communication between the OutputTab and ProjectsTab for toggle state control.

[33mcommit d5d7ca28fccada68871adcec011c613bb2a216de[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Fri Jan 24 17:16:00 2025 +0100

    Refactor progress window for improved independence and behavior
    
    Updated the progress window to be independent and properly configurable, ensuring it appears in the taskbar and behaves without stealing focus. Adjusted parent references, window flags, and callbacks for better process management and interface consistency.

[33mcommit 287e824cba37ab365b9f68d4f1f025f83a89f96e[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Fri Jan 24 16:59:19 2025 +0100

    Update version to 1.2.3 and improve adduct handling logic
    
    Bumped version number in README, changelog, and UI elements to 1.2.3. Added changes to remove invalid adduct spectra and refactored adduct normalization for improved handling. This update ensures better spectrum processing and maintains consistency across the app.

[33mcommit bafbb6ab403af46e0608c51d45e61ceae0e20081[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Fri Jan 24 16:52:45 2025 +0100

    Hide main window during execution and restore it afterwards.
    
    The `open_progress_window` method now hides the main window when the progress window is opened and restores it after execution completes. This ensures a cleaner UI experience by focusing on the progress window during execution.

[33mcommit bdf813bb4c81dd91f6d6acd098a6566618dbe742[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Jan 23 17:09:42 2025 +0100

    Update version to 1.2.2 across application files
    
    Incremented version number from 1.2.1 to 1.2.2 in the README, main application window, and progress window. This ensures consistency in versioning and reflects the latest changes in the application.

[33mcommit c860acb98fd5c86c5f28bb4bf81015d3bc1fc846[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Jan 16 11:59:37 2025 +0100

    Update version to 1.2.1 in README and application windows
    
    Updated the displayed version number across the README and application windows to reflect the new release (1.2.1). This ensures consistency and clarity for users regarding the current version.

[33mcommit acb3c4415c86ea7012b8eccffb03fd2076b9e2b3[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Thu Jan 16 11:57:53 2025 +0100

    Replace error print with full traceback logging
    
    Updated error handling in FragHub.py to log full tracebacks instead of printing error messages, improving debugging clarity. This change uses `traceback.print_exc()` to provide detailed exception information.

[33mcommit 7cbd3abdab8b4a986670aaf800fe8ce6bb609a0b[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Dec 18 14:30:10 2024 +0100

    Add deletion tracking and reporting for duplicate removal
    
    Introduced a deletion callback to track and report the number of duplicates removed in `remove_duplicatas`. Integrated this callback into relevant modules, updated the progress window to display deletion messages, and created a global variable in a new `deletion_report` module to store the count. This improves visibility and transparency of duplicate removal actions.

[33mcommit d3009bbb8fc5fa9e53b5f2cfe13fd786ede09aec[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Dec 18 10:05:26 2024 +0100

    Set application icon and AppUserModelID for FragHub
    
    Added a call to set the application's AppUserModelID for better Windows compatibility. Also updated the GUI to include a custom window icon for the application. These changes enhance the app's integration and user experience on Windows.

[33mcommit 32b4874cf12096e2828385360cc806ed871c93d1[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Wed Dec 18 09:30:09 2024 +0100

    Add completion callback to replace progress bar with message
    
    Introduced a `completion_callback` to handle the replacement of the progress bar with a final message upon completion. Updated `MAIN`, `FragHub`, and `progress_window` to support this functionality, ensuring a smoother user experience and clearer task termination feedback.

[33mcommit cc94b690671f089983ac54cf48d16f79d16d24b8[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Tue Dec 17 16:46:37 2024 +0100

    Add completion callback to replace progress bar with message
    
    Introduced a `completion_callback` to handle the replacement of the progress bar with a final message upon completion. Updated `MAIN`, `FragHub`, and `progress_window` to support this functionality, ensuring a smoother user experience and clearer task termination feedback.

[33mcommit 258941758002b09f11c688a4348159f4b85d9466[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Tue Dec 17 15:50:17 2024 +0100

    Add step tracking feature to progress report
    
    Introduce a new signal `update_step_signal` to track and display progress steps in the "Report" tab. Updated the GUI to handle and render step-specific updates, enabling enhanced user feedback for task progression.

[33mcommit 799acafb2b8c843269d0f11c0065f736449d2a23[m
Author: Axel.Dablanc <axel.dablanc@univ-tlse3.fr>
Date:   Tue Dec 17 09:42:59 2024 +0100

    Rename GUI.py to FragHub.py
    
    This renaming reflects a transition to a more descriptive and specific naming convention. It improves clarity regarding the purpose of the script within the project.
