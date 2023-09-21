# Plate-Availability-Checker
A python script that automatically checks custom/vanity plate availability with the DOT site using input from a .txt file, or the included random generator.
This currently only works for PA, but we are working on implementing other states, as well as a GUI.
<h2>Requirements</h2>
<p>This script requires <a href=https://www.python.org/downloads/">Python<a/>, <a href="https://www.selenium.dev/downloads/">Selenium<a/>, and <a href="https://chromedriver.chromium.org/downloads">Chrome Web Driver<a/> in order to work.<p>
<h2>PlateChecker_withInput(PA).py</h2>
<p>This script takes input from the specified text file, and runs each line through <a href="https://www.dmv.pa.gov/VEHICLE-SERVICES/Registration%20Plates/Pages/Personalized%20Availability.aspx">PennDOT's personalized plate availability checker</a>. </p>
<p>The console prints which plates are available, and unavalable. Available plates are outputted to the specified text file.</p>
<h3>Parameters</h3>
<p>when running the script, a few prompts come up</p>
<p>Input File: file path for .txt input file. Script will create the file if it does not already exist</p>
<p>Output File: file path for .txt output file. Script will create file if it doesn't exist</p>
<p>Headless browser window: asks for (y/n) input. use 'y' if you don't want the chrome tab unavailable</p>
<h2>PlateChecker_withGenerator(PA).py</h2>
