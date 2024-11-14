// https://leetcode.com/problems/to-be-or-not-to-be

type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    
    return {
        toBe: (targetVal: any) => {
            if (val === targetVal)
                return true;
            else
                throw new Error("Not Equal")
        },

        notToBe: (targetVal: any) => {
            if (val !== targetVal)
                return true;
            else
                throw new Error("Equal")
        }
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
