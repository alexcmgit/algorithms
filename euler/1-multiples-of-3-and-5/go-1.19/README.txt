Working dir: euler/1-multiples-of-3-and-5/go-1.19

Run/test all solutions: go run .

[packaging]

Tried my best to find a solution (use multiple packages, modules, etc.) but this is the simplest one I found. The priority of all source files is to keep solutions in their files and a test file which test them. But the solution itself doesnt even know (and should not) they are being tested. 

I've toc, please, all solutions must be named [solution<n>.<ext>] and the test file must be [test.<ext>].

[go.mod] is required to run [go run .] without the need to specify test + each solution itself (go run test.go s1.go s2.go [...]).
