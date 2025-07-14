# uv: A Fast and Modern Python Package and Project Manager

**uv** is a new Python package and project manager built with **Rust**, developed by the creators of **Ruff**. It aims to be a faster and more streamlined alternative to traditional tools like `pip` and `virtualenv`, offering significant improvements in speed and efficiency.

---

### 🔧 Key Features

- **⚡ Lightning-fast performance**:  
  `uv` is significantly faster than `pip`, boasting **10–100× speed improvements** for package installation and dependency resolution — especially for large projects with caching enabled.

- **🧰 Unified Tooling**:  
  Combines the functionality of `pip`, `pip-tools`, `virtualenv`, and others into a single tool, simplifying Python workflows.

- **📦 Built-in Virtual Environment Management**:  
  Automatically creates and manages virtual environments, removing the need for separate tools.

- **🔒 Reliable Dependency Locking**:  
  Supports **universal lock files** for reproducible builds, ensuring consistent environments across different systems.

- **💾 Disk-Space Efficiency**:  
  Uses a **global cache** to deduplicate dependencies and save storage space.

- **🖥️ Cross-Platform Support**:  
  Works on **macOS, Linux, and Windows**.

---

### 🚀 Steps to Use uv

#### 🛠️ Installation

Use the official installer (recommended):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
````

> ℹ️ `pip install uv` is possible but not recommended for system-wide use.

---

#### 📁 Project Initialization

Navigate to your project directory and run:

```bash
uv init
```

This creates a `pyproject.toml` and a `.venv` virtual environment.

---

#### 📦 Dependency Management

* **Add packages**:

  ```bash
  uv add <package-name>
  ```

* **Install from `requirements.txt`**:

  ```bash
  uv add -r requirements.txt
  ```

* **Update packages**:

  ```bash
  uv update <package-name>
  # or
  uv lock -U
  ```

* **Remove packages**:

  ```bash
  uv remove <package-name>
  ```

---

#### ▶️ Running Scripts

Execute scripts within the virtual environment:

```bash
uv run <command>
```

---

#### 🔐 Locking Dependencies

Create or update the lockfile:

```bash
uv lock
```

This generates a `uv.lock` file for **reproducible environments**.

---

### 📊 Comparison: uv vs pip

| Feature                    | `uv`                                        | `pip`                            |
| -------------------------- | ------------------------------------------- | -------------------------------- |
| **Speed**                  | ⚡ 10–100× faster                            | Slower                           |
| **Environment Management** | Built-in                                    | Requires `virtualenv` or similar |
| **Lock Files**             | Universal lock files (`uv.lock`)            | Needs `pip-tools` or `poetry`    |
| **Python Dependencies**    | None (built with Rust)                      | Relies on Python                 |
| **Error Handling**         | Clear, concise messages                     | Often verbose or unclear         |
| **Integration**            | Unified tool, drop-in replacement for `pip` | Primarily handles installations  |

---

### ✅ Conclusion

`uv` offers **speed**, **reliability**, and **unified tooling** to streamline Python development. Its drop-in compatibility with `pip` and focus on performance make it a promising tool for modern Python workflows.