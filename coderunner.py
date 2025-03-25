import os
import subprocess

def start(dir: str):
    for problem_folder in os.listdir(dir):
        problem_path = os.path.join(dir, problem_folder)
        if os.path.isdir(problem_path):
            test_file = os.path.join(problem_path, "test_solution.py")
            if os.path.exists(test_file):
                print(f"Running tests in {problem_folder}...")
                try:
                    subprocess.run(["python", test_file], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"tests in {problem_folder} failed: {e}")
                print("-" * 40)
