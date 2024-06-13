#!/bin/bash

# Imposta il colore del testo
color="\033[38;5;202m"

# Imposta la dimensione del terminale
height=$(stty size | cut -d' ' -f1)
width=$(stty size | cut -d' ' -f2)

# Crea una funzione per disegnare una linea orizzontale di caratteri che cadono dall'alto
draw_line() {
  line=""
  for i in $(seq 1 $1); do
    line+="$color$(printf '\n%*s' "-$((RANDOM % width))" '')"
  done
  echo -e "$line"
}

# Crea una funzione per disegnare una griglia di linee di caratteri che cadono dall'alto
draw_matrix() {
  matrix=""
  for i in $(seq 1 $1); do
    matrix+=$(draw_line $2)"\n"
  done
  echo -e "$matrix"
}

# Crea una funzione per creare l'effetto visivo di Matrix
matrix_effect() {
  while true; do
    matrix=$(draw_matrix $height $width)
    echo -e "$matrix"
    sleep 0.01
    clear
  done
}

# Esegui la funzione matrix_effect
matrix_effect