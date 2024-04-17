# Newton Raphson

## Problems
* Only used open methods, because the function doesn't change sign.
* The derivative goes to zero. (divided by zero): (Rolston and Rabinowitz, 1978) determined that f(x) reach zero before f'(x).
* Newton-Raphson and Secant Methods are linearly convergent for multiple roots.

	 $$ x_{i+1} = x_i - m \frac{f(x_i)}{f\prime(x_i)}$$

	 Where m is the multiplicity of the root.

	They determined that used the ratio of the function and his derivative.

	$$ u(x) = \frac{f(x)}{f\prime(x)}$$

	Because this function has roots at all the same
	locations.

	$$ x_{i+1} = x_i - \frac{u(x_i)}{u\prime(x_i)}$$

	$$ u$$
