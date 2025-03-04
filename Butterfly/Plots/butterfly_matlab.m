% MATLAB script to solve 256 = (N+c)*2^(N-c-1) - c for N as a function of c
% and plot N (y-axis) versus c (x-axis) for c in [0,20].

% Define a vector of c values:
cVals = linspace(0, 20, 201);
Nsol = zeros(size(cVals));  % preallocate solution vector for N

% Set options for fzero to suppress output:
options = optimset('Display', 'off');

% Loop over each c value and solve for N using fzero.
for i = 1:length(cVals)
    c = cVals(i);
    % Define the function handle for the equation f(N) = 0:
    % f(N) = (N+c)*2^(N-c-1) - c - 256
    eqfun = @(N) (N + c) * 2^(N - c - 1) - c - 256;
    
    % For a good initial guess, use the previous solution (or a constant for the first point)
    if i == 1
        N0 = 6.3;  % initial guess for c=0
    else
        N0 = Nsol(i-1);
    end
    
    % Use fzero to solve for N:
    Nsol(i) = fzero(eqfun, N0, options);
end

% Plot the results:
figure;
plot(cVals, Nsol, 'LineWidth', 2);
xlabel('c');
ylabel('log(n)');
title({'Sum before first occurence of c > 256','Solution of 256 = (log(n)+c)*2^{log(n)-c-1} - c'});
grid on;
