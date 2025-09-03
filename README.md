# 📂 File Watcher & Backup Script

This Python script monitors a specified folder (`watched_folder`) for **file system events** such as:

- **Creation:** New files are detected in real time  
- **Modification:** Changes to existing files are tracked  
- **Deletion:** Removed files are recorded  
- **Movement:** File renames and moves are captured  

It uses the [`watchdog`](https://pypi.org/project/watchdog/) library to detect changes in real time.

---

## 🔄 How It Works

When a **new file** is created in the watched folder:

1. **Copy to backup:** The file is automatically copied to `../backup`.  
2. **Log event:** The action is recorded in `Log.txt`, located one directory above the watched folder.

---

## 🗂 Workflow Diagram

```bash
[ Watched Folder ] --(new file)--> [ Backup Folder ] 
      |                   ↑                 |
      └----> Event Logged in Log.txt -------┘
```

---

## ✨ Features

- **Real-time monitoring:** Detect changes as they happen  
- **Automatic backup:** Newly created files are copied instantly  
- **Event logging:** Timestamps for all detected changes  

---

## 📦 Requirements

- **Python:** 3.x  
- **watchdog:** Install with:

  ```bash
  pip install watchdog
  ```

## 🚀 How to Run

### Prepare folders

```bash
project/
├── watched_folder/
├── backup/        (will be created automatically if missing)
├── Log.txt        (will be created automatically)
└── file_watcher.py
```

### Install dependencies

```bash
pip install watchdog
```

### Run the script

```bash
python file_watcher.py
```

Test it: Drop a file: Place any file in watched_folder — it will be backed up and logged.

## 👤 Author

### SirLuciferZ 📅 2025-09-02
