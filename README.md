<h3>Description</h3>
<p>This repository comes with</p>
<ol>
    <li>Basic API authentication</li>
    <li>Session authentication</li>
    <li>Base layout configured</li>
    <li>Basic Blogging on website using sessions</li>
</ol>
<h3>Pre-requisites</h3>
<ol>
    <li>You should have python 3 installed on your system. You can find it here <a href='https://www.python.org/downloads/'>Python download guide</a>, once installed run <code>python -v</code> or <code>python3 -v</code>, no matter which works for you, it should show version 3 being installed. For me <code>python3 -v</code> works so I will be calling python using the keyword <b>python3</b></li>
    <li>Then you need to install python virtual environment utility using command <i>sudo apt install python3.10-venv</i></li>
</ol>
<h3>Steps to use the repository</h3>
<ol>
    <li>Clone the repository</li>
    <li>Rename the file .env.example to .env and populate it with relavant data</li>
    <li>Now create a virtual environment using the command <code>python3 -m venv env</code></li>
    <li>To start the virtual environment, <i>source env/bin/activate</i>, This will start the virtual environment and now you can execute python or pip commands, install utilities etc without actually installing them on your real system</li>
    <li>Run the command <i>pip install -r requirements.txt</i>. This will install all the dependencies by default</li>
    <li>Run the migrations <code>python3 manage.py migrate</code></li>
    <li>Finally start the server using <code>python3 manage.py runserver</code>, this will also hang the terminal while the server is running, to close the server press CTRL+C</li>
</ol>
<h3>How to create an app</h3>
<p>Please follow the following instruction<p>
<ol>
    <li>Run command <i>python3 manage.py startapp <b>appname</b></i>. For example, for a module called leads, <code>python3 manage.py startapp leads</code></li>
    <li>Enlist the newly created app in \settings.py, in the <b>INSTALLED_APP</b> array, include your app, 'leads.apps.LeadsConfig', this is basically what you would have in apps.py file in your newly created app folder, so add it under the comment #CUSTOM APPS</li>
</ol>