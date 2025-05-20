function R = Ry(theta)
%Ry realiza una rotación en un ángulo theta en radianes con respecto al eje y

R =[cosd(theta), 0, sind(theta);
         0, 1, 0;
         -sind(theta), 0, cosd(theta)]


end