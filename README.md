# Nuke_Start_Screen
![nkss_cover_anim_v1_](https://github.com/user-attachments/assets/8a543507-4f7a-463a-8369-ceb1fb12b58c)

---

# Quick Access 🔗
- [Introduction](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#introduction-);
- [Open in Explorer](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#open-in-explorer-);
- [File not found](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#file-not-found-%EF%B8%8F);
- [Installing](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#installing-%EF%B8%8F);
- [Nuke Compatibility](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#nuke-compatibility-%EF%B8%8F);
- [Troubleshooting](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#troubleshooting-%EF%B8%8F);
- [Supporters](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#supporters-);
- [Support me](https://github.com/danilodelucio/Nuke_Start_Screen?tab=readme-ov-file#support-me-);

# Introduction 📌
- **Nuke Start Screen** displays a window containing the last seven recent files when opening Nuke;

![Screenshot 2024-12-14 195049](https://github.com/user-attachments/assets/045863c7-9cf3-4dd6-bd74-656f26c01832)

# Open in Explorer 📁
- Clicking on the folder icon will open the file path in your Explorer;

![Screenshot 2024-12-14 195522](https://github.com/user-attachments/assets/7167ee50-76d9-47e7-a4ff-d522234a6167)

# File not found ⛓️‍💥
- If your Nuke file was removed, renamed or deleted, the file path will display as red, and the buttons will be disabled;

![Screenshot 2024-12-14 195859](https://github.com/user-attachments/assets/f6fc781e-3d1a-4128-a3df-bbf9a9b3905a)

# Installing ⚙️

<details>
<summary><b></b>How to Install</b></summary>

- Click on the green button and download the zip file;

![image](https://github.com/user-attachments/assets/fad7e331-2c07-481b-94f0-e02ed68b3112)

- Go to your **.nuke** directory (usually at `C:\Users\%username%\.nuke`), and extract the content into a folder;

![image](https://github.com/user-attachments/assets/68b350b6-3753-454d-94f2-429f4486f7da)

- Rename the extracted folder to **Nuke_Start_Screen**;

![image](https://github.com/user-attachments/assets/be472f7e-d731-4064-b5b9-69628a7029e9)

- Inside the **Nuke_Start_Screen** folder, you should have all the content inside of it;

![image](https://github.com/user-attachments/assets/12bb73e2-b63f-47a4-a876-22f5b7e1f529)

- Open the **init.py** file (if you don't have it, you can create one); 

![image](https://github.com/user-attachments/assets/db35c52f-cfca-4303-beaf-883469039077)

- Copy the following code and paste it into your **init.py** file, then save and close it;



```python
import nuke

nuke.pluginAddPath('./Nuke_Start_Screen')
```

</details>

# Nuke Compatibility ☢️
- **Nuke Start Screen** was developed in **Nuke 12.1v5** and tested in **Nuke 15.1v4**, so it's designed to work between those Nuke versions;
- It works for commercial and non-commercial versions (except Indie due the Python limitation);

# Troubleshooting 🛠️
If you have feedback, suggestions, or feature requests, please visit the [Discussions](https://github.com/danilodelucio/Nuke_Start_Screen/discussions) page and create a **New Discussion**.
For bugs, please go to the [Issues](https://github.com/danilodelucio/Nuke_Start_Screen/issues) page and create a **New Issue**.

# Supporters 💪
> 😞

# Support me! 🥺

![image](https://github.com/user-attachments/assets/45a4c358-d381-4f80-aacf-dffc997e3b46)

This personal project required significant time and extra hours of hard work to make it available to everyone.
If you find this tool useful, please consider supporting me on [Buy Me A Coffee](https://buymeacoffee.com/danilodelucio). ☕

> _If you donate any amount, please mention this tool (also your preference name if you want to), so your name will appear in the Supporters list above._

You can also share this tool or send me a positive message, it would help me in the same way.

---

Special thanks to Gustavo Goncalves, Marco Silva and Leticia Matsuoka for testing this tool and providing valuable feedback for improvement.

# Cheers! 🥂
