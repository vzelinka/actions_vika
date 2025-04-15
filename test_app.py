from app import Figure

def test_get_angles():
    fig = "трикутник"
    triangle = Figure(fig, 1)
    assert triangle.get_angles() == 3, f"У {fig} має бути 3 кути!" 
