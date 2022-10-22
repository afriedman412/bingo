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