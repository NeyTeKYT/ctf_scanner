from modules.utils import parse_arguments
from modules.runner import resume, start
from modules.config import config
import modules.output as output

target, verbose = parse_arguments()

config.target = target 
config.verbose = verbose

print(f"\n{'='*60}\n")
print(f"        CTF Scanner - Target: {config.target}")
print(f"\n{'='*60}\n")

config.output_folder = output.create_output_folder()

if output.folder_exists:
    resume()
else:
    start()