# Pillow Drift
Monitor your deployed Machine Learning models and system easily.

## Roadmap
- [x] For each categorical data take into account only to five category.
- [x] Generate distribution for continuous data.
- [ ] Create KS test for continuous data and return the p-value and verdict. <--- Idy
- [x] Create Chi 2 test for categorical data and return the p-value and verdict. <--- Mah
- [ ] Refactor the code.
- [ ] Tests are all we need !
- [ ] Make pillowdrift start and stop commands. <--- Mah
- [ ] A board that shows which variables drifted. <--- Ber
- [ ] Logging
- [ ] Typing
- [ ] Styling flake8
- [ ] Precommit hook

## Start the dashbord

```bash
pillowdrift start --configpath="/Users/berangerguedou/projects/pillowdrift/config.yaml" \
                  --datapath-ref="/Users/berangerguedou/projects/pillowdrift/data/sample_reference.csv" \
                  --datapath-cur="/Users/berangerguedou/projects/pillowdrift/data/sample_current.csv" \
                  --datapath-service="/Users/berangerguedou/projects/pillowdrift/data/system.csv" \
                  --host="127.0.0.1" --port="5000"
```

## Stop the dashbord

```bash
pillowdrift stop --host="127.0.0.1" --port="5000"
```
