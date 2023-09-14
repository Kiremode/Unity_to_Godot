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
}