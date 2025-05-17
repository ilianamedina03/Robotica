<<<<<<< HEAD
function R = Rz(psi)
%Rz realiza una rotación en un ángulo theta en radianes con respecto al eje z

R =[sind(phi)*sind(psi) - cosd(phi)*sind(theta)*cosd(psi), sind(phi)*cosd(psi) + cosd(phi)*sind(theta)*sind(psi), cosd(phi)*cosd(theta)]
=======
function R = Rz(theta)
% Rz realiza una rotación en un ángulo theta en radianes con respecto al eje Z.
R = [cos(theta), -sin(theta), 0;
     sin(theta), cos(theta), 0;
     0, 0, 1];
end
>>>>>>> d082daa50045269f62ddb8b35c20a75e50a1f2d6
