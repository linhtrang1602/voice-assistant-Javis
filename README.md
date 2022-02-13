<h1> Voice assistant Javis</h1>
<img src="https://github.com/linhtrang1602/voice-assistant-Javis/blob/master/Javis/assets/images/javis.png" alt="Javis_logo" width="250" />
<p>Jarvis is a voice commanding assistant service in Python 3.8 It can recognize human speech, talk to user and execute basic commands. The app is built to run on Android. The interface of the application is built using KivyMD<br><br>
The following instructions are for Windows users</p>
<h2> The implemented Voice assistant can perform the following tasks:</h2>
<h3> 1. Predicts time</h3>
&emsp;<strong>E.g</strong><br>
&emsp;&emsp;&emsp;&emsp;User: <em>"What time is it?", "What is the date today?</em>
<h3> 2. Tells jokes</h3>
&emsp;<strong>E.g</strong><br>
&emsp;&emsp;&emsp;&emsp;User: <em>"Tell me a joke"</em>
<h3> 3. Opens a web page</h3>
&emsp;<strong>E.g</strong><br>
&emsp;&emsp;&emsp;&emsp;User: <em>"Open Youtube", "Open Facebook"</em>
<h3> 4. Looks up the definition on the internet</h3>
&emsp;<strong>E.g</strong><br>
&emsp;&emsp;&emsp;&emsp;User: <em>"What is blockchain?", "What is Youtube?"</em>
<h3> 5. Plays a song</h3>
&emsp;<strong>E.g</strong><br>
&emsp;&emsp;&emsp;&emsp;User: <em>"Play a song"</em>
<h2> Getting started</h2>
<h3> Setup Jarvis in Windows system</h3>
<h4> Download the Jarvis repo locally:</h4>
<code>git clone https://github.com/linhtrang1602/voice-assistant-Javis</code>
<h4> Change working directory</h4>
<code> cd voice-assistant-Javis</code>
<h4> (Recommended) Create a virtual environment and activate it </h4>
Read more about virtual environment<br>
https://virtualenv.pypa.io/en/latest/
<h5>1. Create the virtual environment named javis_venv in your current directory:</h5>
<code> python -m virtualenv javis_venv</code>
<h5>2. Activate the virtual environment. You will have to do this step from the current directory every time you start a new terminal. This sets up the environment so the new javis_venv Python is used.</h5>
For Windows default CMD, in the command line do:<br>
<code>javis_venv\Scripts\activate</code>
<h4> Setup Jarvis and system dependencies:</h4>
<code> cd Javis<br>
pip install -r requirements.txt</code><br>
If the installation of PyAudio fails, please execute the following command <br>
<code> pip install pipwin </code><br>
<code> pip win install pyaudio</code><br>
So now you can run Javis by<br>
<code> main.py</code>
