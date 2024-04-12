import cv2

# Carrega o classificador pré-treinado para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicia a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura um frame
    ret, frame = cap.read()

    # Converte para escala de cinza para melhor detecção
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos na imagem
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenha um retângulo ao redor de cada rosto detectado
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

    # Exibe o frame resultante
    cv2.imshow('Video', frame)

    # Verifica se a tecla 'q' foi pressionada para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a captura de vídeo e fecha as janelas
cap.release()
cv2.destroyAllWindows()