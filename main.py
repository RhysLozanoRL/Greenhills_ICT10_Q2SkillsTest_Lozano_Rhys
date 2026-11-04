# Element Information
from pyscript import display, document

def check_details(e):
        document.getElementById('result').innerHTML = ' '
        element = document.getElementById('elementsymbol').value
        
        nonmetals = {  "H": {
            'Symbol':'H',
            'Element':'Hydrogen',
            'Atomic Number':'1',
            'Atomic Mass':'1.008'
        },
        "C": {
                'Symbol':'C',
                'Element':'Carbon',
                'Atomic Number':'6',
                'Atomic Mass':'12.011'
            },
        "N" : {
                'Symbol':'N',
                'Element':'Nitrogen',
                'Atomic Number':'7',
                'Atomic Mass':'14.007'
            },
        "O" : {
                'Symbol':'O',
                'Element':'Oxygen',
                'Atomic Number':'8',
                'Atomic Mass':'15.999'
            },
        "P": {
                'Symbol':'P',
                'Element':'Phosphorus',
                'Atomic Number':'15',
                'Atomic Mass':'30.974'
            },
        "S": {
                'Symbol':'S',
                'Element':'Sulfur',
                'Atomic Number':'16',
                'Atomic Mass':'32.065'
            },
        "Se": {
                'Symbol':'Se',
                'Element':'Selenium',
                'Atomic Number':'34',
                'Atomic Mass':'78.96'
            },
        "F": {
                'Symbol':'F',
                'Element':'Fluorine',
                'Atomic Number':'9',
                'Atomic Mass':'18.998'
            },
        "Cl" : {
                'Symbol':'Cl',
                'Element':'Chlorine',
                'Atomic Number':'17',
                'Atomic Mass':'35.453'
            },
        "Br" : {
                'Symbol':'Br',
                'Element':'Bromine',
                'Atomic Number':'35',
                'Atomic Mass':'79.904'
            },
        "I" : {
                'Symbol':'I',
                'Element':'Iodine',
                'Atomic Number':'53',
                'Atomic Mass':'126.90'
            },
        "At" : {
                'Symbol':'At',
                'Element':'Astatine',
                'Atomic Number':'85',
                'Atomic Mass':'210'
            },
        "Ts" : {
                'Symbol':'Ts',
                'Element':'Tennessine',
                'Atomic Number':'117',
                'Atomic Mass':'294'
            },
        "He" : {
                'Symbol':'He',
                'Element':'Helium',
                'Atomic Number':'2',
                'Atomic Mass':'4.0026'
            },
        "Ne" : {
                'Symbol':'Ne',
                'Element':'Neon',
                'Atomic Number':'10',
                'Atomic Mass':'20.180'
            },
        "Ar" : {
                'Symbol':'Ar',
                'Element':'Argon',
                'Atomic Number':'18',
                'Atomic Mass':'39.948'
            },
        "Kr" : {
                'Symbol':'Kr',
                'Element':'Krypton',
                'Atomic Number':'36',
                'Atomic Mass':'83.798'
            },
        "Xe" : {
                'Symbol':'Xe',
                'Element':'Xenon',
                'Atomic Number':'54',
                'Atomic Mass':'131,29'
            },
        "Rn" : {
                'Symbol':'Rn',
                'Element':'Radon',
                'Atomic Number':'86',
                'Atomic Mass':'222'
            },
        "Og" : {
                'Symbol':'Og',
                'Element':'Oganesson',
                'Atomic Number':'118',
                'Atomic Mass':'294'
            }
    }
     
        element_checker = element in nonmetals




        display_message = (f'This element is not a non-metal.', f'{nonmetals.get(element)}')
        
        document.getElementById('result').innerHTML = (display_message[element_checker])