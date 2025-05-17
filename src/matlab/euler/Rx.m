<<<<<<< HEAD
function R = Rx(phi)
%Rx realiza una rotación en un ángulo theta en radianes con respecto al eje X

R =[1, 0, 0;
         0, cosd(phi), -sind(phi);
         0, sind(phi), cosd(phi)]
=======
function R = Rx(theta)
% Rx realiza una rotación en un ángulo theta en radianes con respecto al eje X.
R = [1, 0, 0;
     0, cos(theta), -sin(theta);
     0, sin(theta), cos(theta)];
end
>>>>>>> d082daa50045269f62ddb8b35c20a75e50a1f2d6
