import multiprocessing
import subprocess

if __name__ == "__main__":
    services = ["data_process_service"]

    services_path = [f"services/{service}.py" for service in services]

    server_scripts = [f"services/user_service.py"]

    processes = []
    for service in services_path:
        print(f"Executing {service}")
        process = multiprocessing.Process(target=subprocess.run, args=(["python", service],))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
