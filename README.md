# Pillow Drift
Monitor your deployed Machine Learning models and system easily.

## Roadmap
- [x] For each categorical data take into account only to five category.
- [x] Generate distribution for continuous data.
- [ ] Create KS test for continuous data and return the p-value and verdict. <--- Mah
- [x] Create Chi 2 test for categorical data and return the p-value and verdict. <--- Mah
- [ ] Refactor the code.
- [ ] Tests are all we need !
- [ ] A board that shows which variables drifted. <--- Ber
- [ ] Logging
- [ ] Typing
- [ ] Styling flake8


## Start the dashboard
Make this command in any terminal
```bash
pillowdrift start --configpath="/Users/berangerguedou/projects/pillowdrift/config.yaml" \
                  --datapath-ref="/Users/berangerguedou/projects/pillowdrift/data/sample_reference.csv" \
                  --datapath-cur="/Users/berangerguedou/projects/pillowdrift/data/sample_current.csv" \
                  --datapath-service="/Users/berangerguedou/projects/pillowdrift/data/system.csv" \
                  --host="127.0.0.1" --port="5000"
```
Or this one in pillowdrift repository
```bash
make pillowstart
```


## Stop the dashboard

Make this command in any terminal
```bash
pillowdrift stop --host="127.0.0.1" --port="5000"
```

Or this one in pillowdrift repository

```bash
make pillowstop
```
