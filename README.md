## Raspberry Pi 4 BrailleSense Project Setup 

This guide outlines setting up a virtual environment for your Raspberry Pi 4 camera project, considering two approaches:

### 1. Using System-Wide Libraries for Camera and GPIO Control

**Requirements:**

* Raspberry Pi 4
* Raspberry Pi Camera Module 2 (compatible with Pi 4)

**1.1. Create Virtual Environment (System-Site Packages):**

Here, we create a virtual environment named `my-env` that utilizes system-wide libraries for camera control and GPIO pins. This might be necessary if your project requires specific system-wide libraries:

```bash
python -m venv --system-site-packages my-env
```

**1.2. Activate Virtual Environment:**

Activate the newly created environment:

```bash
source my-env/bin/activate
```

**1.3. Install Dependencies:**

Install required packages from your `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**2. Exploring picamera2 Features**

For projects requiring extensive camera functionalities or for learning purposes, you can choose to install `picamera2` specifically within the virtual environment.

**2.1. Install `picamera2` (Optional):**

Within the activated virtual environment, install `picamera2`:

```bash
pip install picamera2
```

**3. Resources:**

For an in-depth understanding of `picamera2` features, refer to the official documentation:

* **picamera2 Manual:** [https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)

**Notes:**

* Remember to adjust the virtual environment name (`my-env`) and package names in `requirements.txt` according to your project needs.
* Using system-wide libraries comes with potential risks of conflicts. Consider isolated virtual environments if possible.
* Always exercise caution when modifying system-wide libraries and packages.

By following these steps, you can effectively set up your Raspberry Pi 4 camera project with a virtual environment, catering to both system-wide library usage and exploring `picamera2` specifically.
