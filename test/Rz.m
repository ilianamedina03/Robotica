function R = Rz(psi)
%Rz realiza una rotación en un ángulo theta en radianes con respecto al eje z

R =[cosd(psi), -sind(psi), 0;
         sind(psi), cosd(psi), 0;
         0, 0, 1];

end