# This tool makes it easy to download a ready to use gitignore file



import sys
import os


QUERY_URL = 'https://www.gitignore.io/api/'
SOFT_URL = 'https://www.gitignore.io/api/list'

def usage():

    print("[+] Usage Example :")
    print('\n')
    print("$ python3 ignoreit.py [.gitignore] emacs,node,vagrant \n")
    print(f"[-] For a complete list of software : {SOFT_URL}" )


def ignoreit():

    if len(sys.argv) <= 1:
        usage()
        return

    filename = sys.argv[1]
    raw_args = sys.argv[2]

    
    task_url = QUERY_URL + raw_args


    os.system(f"wget {task_url} -O {filename} " )
    print(task_url)
    



    
if __name__ == '__main__':
    ignoreit()
