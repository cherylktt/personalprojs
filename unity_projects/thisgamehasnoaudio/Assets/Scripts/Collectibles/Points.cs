using UnityEngine;
using UnityEngine.UI;

public class Points : MonoBehaviour
{
    [SerializeField] private Text pointsText;
    private int points = 0;

    private void OnTriggerEnter2D(Collider2D collision){
        if(collision.gameObject.CompareTag("Points")){
            Destroy(collision.gameObject);
            points++;
            pointsText.text = "x " + points;
        }
    }
}
