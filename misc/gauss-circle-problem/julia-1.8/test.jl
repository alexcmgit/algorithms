# Note: This is my first Julia script along with my first Julia solution [solution.jl].
# Julia seems to be pretty easy, intuitive and similar to Python.
# This implementation is probably a horror show for those working with Julia longer, but letsgoo.

include("solution1.jl")

using Test

import .Solution1 as s1

stdfilelines(name) = readlines(joinpath(@__DIR__, "..", name))

stdinlines = stdfilelines("stdin.txt")
stdoutlines = stdfilelines("stdout.txt")

function runtests(tests)
    for test in tests
        id = replace(string(nameof(test)), r"\D+" => "")
        @testset "Test suite of solution $id." begin
            test(stdinlines, stdoutlines, id)
        end
    end
end

function tests1(stdinlines, stdoutlines, id)
    for (index, input) in enumerate(stdinlines)
        # ok, that's a bit weird, julia's array are 1-based.
        println("Running case $index on solution $id.")

        r = C_NULL

        if startswith(input, "sqrt")
            (_, operand) = split(input, " ")
            r = sqrt(BigFloat(parse(Float64, operand)))
        else
            r = BigFloat(parse(Float64, input))
        end

        expected = BigFloat(parse(Float64, stdoutlines[index]))
        output = s1.points(r)

        @testset "Expecting $expected but got $output on solution $id when input is r=$r." begin
            @test output == expected
        end
    end
end

# See [tests1] for details on how you should write the test for your solution.
testers = [tests1]

runtests(testers)