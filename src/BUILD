package(default_visibility = ["//visibility:public"])

py_app(
    name = "app",
    srcs = ["app.py"],
) 
#create an examples test using bazel for app.py 

filegroup(
    name = "srcs",
    srcs = ["BUILD"] + glob(["**/*.py"]),
)
