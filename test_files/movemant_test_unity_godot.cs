using System.Collections;
using System.Collections.Generic;
using Godot;

public partial class test : Node
{
    // This is your speed variable
    [Export]
	public float speed = 10.0f;
    private float y;

    // Update is called once per frame
    public override void _Process(float delta)
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(moveHorizontal, 0.0f, moveVertical);

        // Here we use the speed variable
        transform.position += movement * speed * Time.deltaTime;
    }
}