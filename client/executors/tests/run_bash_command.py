import sys
import os
from client.executors.api.api_processor_facade import api_processor_facade
from client.executors.api.api_processor import ApiSource

sys.path.append('/Users/karanveersinghsirohi/DrDroidLabs/data-droid')


def run_bash_command(command):
    # Get the registered bash API processor
    bash_processor = api_processor_facade.get_source_api_processor(ApiSource.BASH)

    # Execute the bash command
    result = bash_processor.execute_http_get_api(command)

    # Print the result
    print("Command Output:")
    print("STDOUT:", result["stdout"])
    print("STDERR:", result["stderr"])
    print("Return Code:", result["returncode"])


if __name__ == "__main__":
    command = 'ls -l'
    run_bash_command(command)
