# The mapping of Unity's function names to Godot's function names
#look_up = {
#    "void Start()":"public override void _Ready()",
#    "void Update()":"public override void _Process(float delta)",
#    "void FixedUpdate()":"public override void _PhysicsProcess(float delta)",
#    "void Awake()":"public override void _Ready()",
#    "void LateUpdate()":"public override void _PhysicsProcess(float delta)",
#    "void OnDisable()":"public override void _ExitTree()",
#    "void OnEnable()":"public override void _EnterTree()",
#    "void OnDestory()":"public override void _ExitTree()",
#
#    "public void Start()":"public override void _Ready()",
#    "public void Update()":"public override void _Process(float delta)",
#    "public void FixedUpdate()":"public override void _PhysicsProcess(float delta)",
#    "public void Awake()":"public override void _Ready()",
#    "public void LateUpdate()":"public override void _PhysicsProcess(float delta)",
#    "public void OnDisable()":"public override void _ExitTree()",
#    "public void OnEnable()":"public override void _EnterTree()",
#    "public void OnDestory()":"public override void _ExitTree()",
#
#    "private void Start()":"public override void _Ready()",
#    "private void Update()":"public override void _Process(float delta)",
#    "private void FixedUpdate()":"public override void _PhysicsProcess(float delta)",
#    "private void Awake()":"public override void _Ready()",
#    "private void LateUpdate()":"public override void _PhysicsProcess(float delta)",
#    "private void OnDisable()":"public override void _ExitTree()",
#    "private void OnEnable()":"public override void _EnterTree()",
#    "private void OnDestory()":"public override void _ExitTree()",
#}
#i = 0
## Function to convert Unity's function to Godot's function
#def convert_function(function_name):
#    # Remove the access modifier
#    function_name = function_name.replace("public ", "").replace("private ", "").replace("void ", "")
#    
#    
#    # Check if the function name is in the look_up dictionary
#    if function_name in look_up:
#        print(function_name)
#        return look_up.items()[i][1]
#    else:
#        return function_name
#
#
def look_up_table(input_code):
    access_modifiers = ["void", "public void", "private void"]
    methods = ["Start()", "Update()", "FixedUpdate()", "Awake()", "LateUpdate()", "OnDisable()", "OnEnable()", "OnDestory()"]
    godot_methods = ["_Ready()", "_Process(float delta)", "_PhysicsProcess(float delta)", "_Ready()", "_PhysicsProcess(float delta)", "_ExitTree()", "_EnterTree()", "_ExitTree()"]

    look_up = input_code

    for modifier in access_modifiers:
        for method, godot_method in zip(methods, godot_methods):
            look_up[f"{modifier} {method}"] = f"public override void {godot_method}"

    print(look_up)
    return look_up