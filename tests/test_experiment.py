from src.generate_experiment import generate_experiment

def test_shape():
    df=generate_experiment(1000,1)
    assert len(df)==1000

def test_randomization():
    df=generate_experiment(10000,2)
    assert .47 < df.treatment.mean() < .53
