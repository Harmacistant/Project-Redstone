# Project-Redstone
This is my personal project to learn some practical python and get back into modding minecraft.  Sure, there are launchers out there that do the same thing, but some require you to have accounts with 3rd parties, or will track your usage, etc.

This is _not_ a launcher - simply a mod manager.  The idea here is to use the vanilla launcher for anything and everything possible, and not be _required_ to download a launcher.

Project Goals:

* Simplify the creation of minecraft modpacks
    * Upon creation, simply specify the version of minecraft to be used in the modpack.
    * From there, list mods that are compatible with the version specified
    * Allow for auto-dependency and conflict resolution when simply dragging and dropping mods into a folder.
        * If a mods folder is open, and you start moving mods, it will check if the version is correct for the version of minecraft being used, get dependencies, check for conflicts and updates, etc.
* Simplify mod and dependency management
    * Once a mod has been selected, all of its necessary dependencies will be added automatically.
    * If a dependency cannot be added, for whatever reason, the mod will be flagged for review.
    * Should a mod no longer be desired, it can be removed and all dependencies for it will be flagged.
        * Any dependency that is shared will be flagged for review.
        * All other dependencies will be flagged for removal.
    * Mods with known conflicts with other selected mods will throw warnings.
        * Known workarounds will be offered (ie ID conflicts, config changes, etc) and implemented if selected.
        * Mods with no known workarounds for conflicts will display the known issues for all conflicting mods.
* Manage Installations
    * Maintain an orderly folder for mod management
        * Supported folder organizations will include:
            1) Alphabetical by File Name
            2) Alphabetical by Mod Name
            3) Hierarchical (Parent mod followed by dependencies)
            4) Custom Ordering
            5) Manual/No Ordering
    * Allow for export to zip files for easy sharing among friends
        * Potentially include python script for easy install with zip?
* Manage Auto-Updating
    * Run as a service to check for newer versions of mods by the version of minecraft they support
    * Allow for the following auto-update options:
        * Full world/server backup before updates are applied
        * Automatically test for singleplayer/server launch success
            * Restore or warn upon failures
        * Automatically update all versions
        * Automatically update to minor versions, prompt for major
        * Automatically update all versions that are % previous size or smaller
            * (ie if a current file is 100kb and the new file is 110kb and the threshold is 10%, autoupdate)
        * Warn for major file content changes
            * (ie if a new file would be 50% larger than the current file, or 30% smaller, etc.)
        * Retain all versions of updated mods for support/failover purposes
        * Per-Mod Auto-update settings
        * Only auto-update at specific date/times if there are new files available
        * Shutdown servers for automatic updates and restart
            * If a failure is detected, restore the server to its previous state