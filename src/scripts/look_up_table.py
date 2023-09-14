# I know that this is stupit but it works and all the other trash i tried did not work so this is what we are doing

#this is a look up table that is used to replace the unity code with the godot code
look_up ={
    "using UnityEngine;":"using Godot;",
    "void Start()":"public override void _Ready()",
    "void Update()":"public override void _Process(float delta)",
    "void FixedUpdate()":"public override void _PhysicsProcess(float delta)",
    "void Awake()":"public override void _Ready()",
    "void LateUpdate()":"public override void _PhysicsProcess(float delta)",
    "void OnDisable()":"public override void _ExitTree()",
    "void OnEnable()":"public override void _EnterTree()",
    "void OnDestory()":"public override void _ExitTree()",

    "public void Start()":"public override void _Ready()",
    "public void Update()":"public override void _Process(float delta)",
    "public void FixedUpdate()":"public override void _PhysicsProcess(float delta)",
    "public void Awake()":"public override void _Ready()",
    "public void LateUpdate()":"public override void _PhysicsProcess(float delta)",
    "public void OnDisable()":"public override void _ExitTree()",
    "public void OnEnable()":"public override void _EnterTree()",
    "public void OnDestory()":"public override void _ExitTree()",

    
    "private void Start()":"public override void _Ready()",
    "private void Update()":"public override void _Process(float delta)",
    "private void FixedUpdate()":"public override void _PhysicsProcess(float delta)",
    "private void Awake()":"public override void _Ready()",
    "private void LateUpdate()":"public override void _PhysicsProcess(float delta)",
    "private void OnDisable()":"public override void _ExitTree()",
    "private void OnEnable()":"public override void _EnterTree()",
    "private void OnDestory()":"public override void _ExitTree()",
}