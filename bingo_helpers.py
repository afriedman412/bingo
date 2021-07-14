html_header = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>F1 Bingo Card Generator</title>
            <script>
            var count=1;
            function setColor(btn, color){
                var property = document.getElementById(btn);
                if (count == 0){
                    property.style.backgroundColor = "#FFFFFF"
                    property.style.color = "#000000"
                    count=1;        
                }
                else{
                    property.style.backgroundColor = "#000000"
                    property.style.color = "#FFFFFF"
                    count=0;
                }

            }
            </script>
        </head>
        <style>

            @font-face {
              font-family: 'Formula1';
              src: url('Formula1-Display-Regular.woff') format('woff'), /* Modern Browsers */
                   local('Formula1-Regular.ttf')  format('truetype') /* Safari, Android, iOS */
            }

            body {
              margin: 40px;
              font-family: Arial, Helvetica, sans-serif;
            }

            .box {
              background-color: white;
              border-style: solid;
              border-color: #e10600;
              border-width: 4px;
              color: black;
              border-radius: 5px;
              padding: 10px;
              font-size: 75%;
              text-align: center;
            }

            .hed {
                background-color: black;
                font-family: "Formula1";
                font-size: xx-large;
                color: #fff;
                border-radius: 5px;
                padding: 10px;
                text-align: center;
                width: 520px;
                margin-bottom: 10px;
            }

            .wrapper {
              width: 600px;
              display: grid;
              grid-gap: 10px;
              grid-template-columns: repeat(5, 100px);
              grid-template-rows: repeat(5, 100px);
              grid-auto-flow: column;

            }
        </style>

        <div class="hed" id="headr">VROOMATES F1 BINGO</div>

        """

html_tail = """
        </body>
        </html>
"""
teams = [
        "Mercedes", "Ferrari", "Red Bull", "Alpha Tauri",
        "Haas", "Aston Martin", "Alfa Romeo", "Williams",
        "McLaren", "Alpine"
    ]

generic = [
        "{} investigated by race control",
        "Shot of {} pit crew", 
    ]

unique = [
        "Lewis micromanages", 
        "Beep'd out radio", 
        "Ferrari infighting", 
        "5 second penalty", 
        "Pit stop under 2 seconds", 
        "Pit stop over 4 seconds", 
        "Speculation about second Mercedes seat 2022", 
        "“Debris”", 
        "Fun fact about host country", 
        "Wing damage", 
        "Tire damage", 
        "Yellow flag", 
        "Red flag",
        "Brakes smoke or catch fire",
        "Haas does some Haas shit",
        "Race control notes (but doesn't investigate)",
        "Max unintelligible on the radio", 
        "“Marbles”", 
        "Mention someone’s dad", 
        "Show someone’s dad", 
        "“Box box box”", 
        "Show a POC not related to a driver", 
        "Driver told to switch plans",
        "3+ DNFs", 
        "“Penultimate”",
        "Christian Horner jiggling foot", 
        "Blue flag penalty", 
        "Toto Wolff extreme closeup", 
        "“Chicane”",
        "Safety car (real)!!!",
        "Safety car (virtual)!!!",
        "Mention Kimi's age or longevity",
        "Senna mentioned",
        "Jensen Button mentioned",
        "Discussion of a driver doing an extremely rich person activity",
        "“Downforce”",
        "Driver comments on wind",
        "DRS overtake",
        "Spinout",
        "Driver asks permission to pass teammate",
        "Stop/go penalty"
        ]