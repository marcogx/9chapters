def single_number_three(nums):
    pass

"""
public int singleNumber(int[] nums) {
    // input check
    int[] bits = new int[32];
    for (int num: nums) {
        for (int i = 0; i < 32; i++) {
            bits[i] += (num & 1);
            num >>= 1;
        }
    }

    int res = 0;
    for (int i = 0; i < 32; i++) {
        res += (bits[i] % 3) << i;
    }
    return res;
}

"""