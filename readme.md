


<h1 align="center">
📖 ft_stockholm - 42 Cibersecurity
</h1>

<p align="center">
	<b><i>Ft_wannacry</i></b><br>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Falitomal/ft_stockholm?color=lightblue" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/Falitomal/ft_stockholm?color=yellow" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Falitomal/ft_stockholm?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Falitomal/ft_stockholm?color=green" />
</p>

## 💡 About the project

# ft_stockholm - Educational Ransomware Simulator

A Linux-based educational program that simulates WannaCry ransomware behavior for cybersecurity learning purposes. This project demonstrates file encryption, decryption, and secure key management.

## ⚠️ Disclaimer

This project is **strictly for educational purposes** in a controlled environment. You must:
- Use a virtual machine or Docker container
- Never use this program for malicious purposes
- Have explicit authorization before testing on any system

## 📋 Features

- **Secure Encryption**: Uses Fernet (symmetric encryption) from the cryptography library
- **Selective Targeting**: Only encrypts files with WannaCry-affected extensions in `~/infection/` directory
- **Reversible**: Can decrypt files with the correct encryption key
- **Silent Mode**: Optional quiet operation for batch processing
- **Error Handling**: Gracefully handles permission errors and corrupted files

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7+
- Cryptography == 46.0.3
- Write access to home directory

### Setup

```bash
make all          # Create virtual environment
make install      # Install dependencies
make run          # Execute program
```

### Command Line Options

```bash
# Display help
./stockholm.py -h / --help

# Show version
./stockholm.py -v / --version

# Encrypt files (generates stokholm.key)
./stockholm.py

# Decrypt files with key
./stockholm.py -r <encryption_file.key>

# Silent mode (no output)
./stockholm.py -s
```

### Examples

```bash
# Encrypt files in ~/infection/ with silent mode
python -m stockholm -s

# Decrypt using saved key
python -m stockholm -r <key_from_stokholm.key>

# View help information
python -m stockholm -h
```

## 📁 Project Structure

- `src/main.py` - Entry point
- `src/manager/__init__.py` - Command-line argument parsing
- `src/ransomwarer/__init__.py` - Core encryption/decryption logic
- `src/constants.py` - Configuration and constants
- `requirements.txt` - Python dependencies
- `Makefile` - Build and run automation
- `stokholm.key` - Generated encryption key (created during first run)

## 🔐 Security Details

- **Algorithm**: Fernet (symmetric encryption with authentication)
- **Key Length**: Minimum 16 characters
- **Target Directory**: `~/infection/` only
- **Extension**: `.ft` appended to encrypted files
- **Supported Formats**: WannaCry affected file extensions (.doc, .docx, .xls, .xlsx, .ppt, .pdf, etc.)

## ⚙️ Makefile Targets

- `make all` - Create virtual environment
- `make install` - Install dependencies
- `make run` - Run the program
- `make clean` - Remove artifacts
- `make fclean` - Full cleanup including venv
- `make re` - Rebuild everything

## 📝 Notes

- Encryption key is saved to `stokholm.key` during first execution
- Keep the encryption key safe—without it, decryption is impossible
- Program skips files without WannaCry extensions
- All operations logged unless `-s` flag is used