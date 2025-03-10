function R = Rz(psi)
%Rz realiza una rotación en un ángulo theta en radianes con respecto al eje z

R =[sind(phi)*sind(psi) - cosd(phi)*sind(theta)*cosd(psi), sind(phi)*cosd(psi) + cosd(phi)*sind(theta)*sind(psi), cosd(phi)*cosd(theta)]