import os
from pathlib import Path
from credentials import credentials
import paramiko


def upload_files(sftp, local_directory, remote_directory):
    for root, _, files in os.walk(local_directory):
        striped_root = root[len(str(local_directory)) + 1:]
        remote_root = Path(
            str(remote_directory.as_posix()) + '/' + striped_root)
        try:
            sftp.listdir(remote_root.as_posix())
        except FileNotFoundError:
            sftp.mkdir(remote_root.as_posix())

        for file in files:
            local_file = os.path.join(root, file)
            remote_file = Path(os.path.join(remote_root, file)).as_posix()
            sftp.put(local_file, remote_file)


def main():
    local_directory = Path('output')
    remote_directory = Path('./www')

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            hostname=credentials['url'],
            username=credentials['username'],
            password=credentials['password'],
        )
        sftp = ssh.open_sftp()
        upload_files(sftp, local_directory, remote_directory)
        sftp.close()
    finally:
        ssh.close()


if __name__ == "__main__":
    main()
