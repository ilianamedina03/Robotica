function R = Rx(phi)
%Rx realiza una rotación en un ángulo theta en radianes con respecto al eje X

R =[1, 0, 0;
         0, cosd(phi), -sind(phi);
         0, sind(phi), cosd(phi)];
end