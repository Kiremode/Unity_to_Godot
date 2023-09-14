using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public partial class test : Node
{
    // This is your speed variable
    [Export]
	public float speed = 10.0f;
    private float y;

    // Update is called once per frame
    public public override void _Process(float delta)
    {
         
        Vector2 inputDir = Input.GetVector("ui_left", "ui_right", "ui_up", "ui_down");

        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);

        // Here we use the speed variable
        transform.position += movement * speed * Time.deltaTime;
    }
}