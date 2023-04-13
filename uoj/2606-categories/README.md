<p><a href="https://www.beecrowd.com.br/repository/UOJ_2606_en.html">beecrowd.com.br/repository/UOJ_2606_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2606</span>
                                    <h1>Categories</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brazil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>When the data were migrated to the database, there was a small misunderstanding on the DBA.</p>
                                    <p>Your boss needs you to select the ID and the name of the products, whose categorie name start with 'super'.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>products</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>amount</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>price</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>id_categories (FK)</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>categories</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>name</td>
                              <td>varchar</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>products</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>amount</strong></td>
                      <td><strong>price</strong></td>
                      <td><strong>id_categories</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Lampshade</td>
                      <td>100</td>
                      <td>800</td>
                      <td>4</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Table for painting</td>
                      <td>1000</td>
                      <td>560</td>
                      <td>9</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Notebook desk</td>
                      <td>10000</td>
                      <td>25.50</td>
                      <td>9</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Computer desk</td>
                      <td>350</td>
                      <td>320.50</td>
                      <td>6</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Chair</td>
                      <td>3000</td>
                      <td>210.64</td>
                      <td>9</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Home alarm</td>
                      <td>750</td>
                      <td>460</td>
                      <td>4</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>categories</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>old stock</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>new stock</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>modern</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>commercial</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>recyclable</td>
                </tr>
                <tr>
                  <td>6</td>
                  <td>executive</td>
                </tr>
                <tr>
                  <td>7</td>
                  <td>superior</td>
                </tr>
                <tr>
                  <td>8</td>
                  <td>wood</td>
                </tr>
                <tr>
                  <td>9</td>
                  <td>super luxury</td>
                </tr>
                <tr>
                  <td>10</td>
                  <td>vintage</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>id</strong></td>
          <td><strong>name</strong></td>
        </tr>
        <tr>
          <td>2</td>
          <td>Table for painting</td>
        </tr>
        <tr>
          <td>3</td>
          <td>Notebook desk</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Chair</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>