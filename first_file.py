import sys

def main():
    script = sys.argv[0]
    option = sys.argv[1]
    config_file = sys.argv[2]

    print(f' \n script {script} wird '
          f' \n mit option {option} \n '
          f'an dem configuration file "{config_file}" ausgeführt')

if __name__ == '__main__':
   main()