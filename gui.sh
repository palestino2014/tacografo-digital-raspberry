yad --list --title='VELOCIDADE' --height=400 --width=250 --column='CM/S'  $(cat velocidade.txt | cut -d ':' -f 1)
