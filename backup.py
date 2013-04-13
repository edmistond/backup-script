#!/usr/local/bin/python

from os import path
import sys
import subprocess

backup_destination_path = "/Volumes/FreeAgent/rsync_test"


def check_backup_path():
    """
    make sure the destination path exists!
    """
    return path.exists(backup_destination_path)


def get_backup_paths():
    """
    returns a collection of backup source paths
    """

    return ["/Users/edmistond/Documents",
            "/Users/edmistond/photos",
            "/Users/edmistond/projects",
            "/Users/edmistond/.vim",
            "/Users/edmistond/Downloads",
            "/Users/edmistond/.ssh",
            "/Users/edmistond/.bash_profile",
            "/Users/edmistond/Music"]


def build_rsync_command(target_path):
    return ["rsync", "-va", target_path, backup_destination_path]


def main():
    if not check_backup_path():
        print "\n\nThe backup path does not exist. Is the drive connected and mounted?\n\n"
        sys.exit(-1)

    backup_paths = get_backup_paths()

    for bp in backup_paths:
        print "\n\n *** backing up: %(bp)s" % {"bp": bp}
        subprocess.call(build_rsync_command(bp))


if __name__ == '__main__':
    main()
    sys.exit(0)
