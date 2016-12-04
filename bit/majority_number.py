"""
public int majorityElement(int[] nums) {
    // input check
    int[] bits = new int[32];
    for (int num: nums) {
        for (int i = 0; i < 32; i++) {
            bits[i] += num & 1;
            num >>= 1;
        }
    }

    int res = 0, len = nums.length;
    for (int i = 0; i < 32; i++) {
        if (bits[i] > len / 2) {
            res += 1 << i;
        }
    }
    return res;
}
"""