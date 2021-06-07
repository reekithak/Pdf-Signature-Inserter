# Pdf-Signature-Inserter
The Application basically helps you in inserting signatures over to given forms or pdf's. <br/>

## Functionality 

- Its a application focussed to insert buyer's and seller's signatures into forms.
- It was made as a part of a requirement to automate the above purpose.
- The coordinates need to be given externally ( as in where to insert the buyer's and seller's singatures respectively ).
- The coordinates can be calculated, easily 

### Image Space within a pdf
- Identify Coordinates
- Base here : X = 36x1 -> 500x1  (Finishing)
- Base here : Y =  36y1 -> 739y1 (Finishing)
- Finishing > Within the boundaries
- ^ For all Pages ? ->  (Slight Differences , Adjustable )

### IMAGE DETAILS


BUYER<br/>
- 1st : - "7x125x220x100x40"
- 2nd : - "7x125x150x100x40"

SELLER<br/>
- 1st : - "7x340x220x100x40"
- 2nd : - "7x340x150x100x40"
- pdf_fh = open(r"forms.pdf", 'rb')

## Run the Application on your Device ?

### Step 1:
Install [Python 3.7](https://www.python.org/downloads/release/python-370/)  
Don't forget to add Path o Environment Varibales [Doubt?](https://www.educative.io/edpresso/how-to-add-python-to-path-variable-in-windows)

Completely Optional:
Install [Git](https://git-scm.com/downloads)

### Step 2:
Clone this Repository [Tutorial](https://www.youtube.com/watch?v=O72FWNeO-xY)

### Step 3:
From the root folder of the repository, open a commandline terminal/powershell and run the following commands:<br />

`pip install virtualenv` :- Installs Virtualenv Python Module<br />
`virtualenv ANY_NAME` :- Replace ANY_NAME with your choice of environment name<br />
`.\ANY_NAME\Scripts\activate` :- Activates the Virtual Environment we just created<br />
`pip install -r requirements.txt` :- Installs the Required Liraries , Takes time & Needs Space ("A lot")<br />

### Step 4:
Once all the Above is Completed , Lets run our Application.<br\>
Run the below command in the cmd.

`python app.py`
