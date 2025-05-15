function compress(chars: string[]): number {
    let curr;
    let cons = 1;  // consecutive letters
    let i = 0;

    chars.push('🎉'); // Dummy char so that it processes the last set of repeating letters

    for (let j = 1; j < chars.length; j++) {
        curr = chars[j];
        if (curr === chars[j-1]) {
            cons++;
        } else {
            // Overwrite chars with the previous character
            chars[i++] = chars[j-1];

            // Overwrite chars array with cons, taking as many slots as digits
            if (cons >= 2) {
                let strCons = String(cons);
                for (let k = 0; k < strCons.length; k++)
                    chars[i++] = strCons[k];
            } 
            
            cons = 1;

        }
    }

    return i;
};
