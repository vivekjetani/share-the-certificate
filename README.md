# share the certificate

Welcome to the **share the certificate**! This project streamlines the process of converting images to PDFs and sharing certificates via email. 🚀

---

## 📂 Repository Structure

```
📦 certificate-automation
├── 📂 Image
│   └── (Place your certificate images here as JPG files)
├── 📂 output_pdfs
│   └── (Converted PDFs will be stored here)
├── 📄 sheet.csv
│   └── (Recipient details: full name and email address)
├── 📄 index.html
│   └── (HTML template for the email body)
├── 📄 image_to_pdf.py
│   └── (Script to convert images to PDFs)
├── 📄 send_email.py
│   └── (Script to email certificates)
└── 📄 README.md
```

---

## ✨ Features

- 🖼️ **Image to PDF Conversion**: Automatically convert JPG certificates into PDF format.
- 📧 **Email Automation**: Personalize and email certificates to recipients.
- 🛠️ **Customizable**: Easy-to-edit HTML email templates and recipient lists.

---

## 🚀 How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/certificate-automation.git
   ```

2. **Navigate to the Repository**
   ```bash
   cd certificate-automation
   ```

3. **Set Up Dependencies**
   - Install the required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```

4. **Add Certificate Images**
   - Place JPG files in the `Image/` directory.

5. **Edit Recipient List**
   - Update `sheet.csv` with recipient details (columns: `full name`, `email`).

6. **Run Scripts**
   - Convert images to PDFs:
     ```bash
     python image_to_pdf.py
     ```
   - Send certificates via email:
     ```bash
     python send_email.py
     ```

---

## 🛡️ Security Notes

- Replace placeholders in `send_email.py` with your email credentials.
- Use environment variables or secret management tools for better security.

---

## 🤝 Contributing

We welcome contributions! 🧑‍💻

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. 📝

---
