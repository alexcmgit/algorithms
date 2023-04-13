module Solution1

const DEFAULT_PRECISION = BigInt(10)

function compute(r::BigFloat, i::BigInt)
    return floor(BigFloat(r^2 / BigInt(4 * i + 1))) - floor(BigFloat(r^2 / (BigInt(4 * i + 3))))
end

function summation(r::BigFloat, precision::BigInt=DEFAULT_PRECISION)
    sum::BigFloat = 0.0

    for i in 0:precision
        sum += compute(r, i)
    end

    return sum
end

function points(r::BigFloat, precision::BigInt=DEFAULT_PRECISION)
    return 1 + 4 * summation(r, precision)
end

# 128/256 -> sqrt(17) fails to 16.99999999999999999999999999999999999991
# 512 -> sqrt(20) fails to 19.999999999999999999999...76
# 1024 -> finally... it works.
setprecision(BigFloat, 1024)

export points

end
